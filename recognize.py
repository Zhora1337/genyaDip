from openalpr import Alpr
import sys

def recognize(path):
    alpr = Alpr("ru", "./ru.conf", "./openalpr/runtime_data") 
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)
    
    alpr.set_top_n(20)
    alpr.set_default_region("ru")

    results = alpr.recognize_file(path)

    i = 0
    for plate in results['results']:
        i += 1
        print("Plate #%d" % i)
        print("   %12s %12s" % ("Plate", "Confidence"))
        for candidate in plate['candidates']:
            prefix = "-"
            if candidate['matches_template']:
                prefix = "*"
            if ((len(candidate['plate'])==6 and (int(candidate['confidence'])>80))):
                print(candidate['plate'])
                return candidate['plate']
# Call when completely done to release memory
    alpr.unload()
    return 'filed'