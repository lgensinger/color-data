# hacky way to allow sibling imports without setting up real packages for DEV purposes
if __name__ == "__main__":
    
    import sys
    from os import path

    # modify sys path 
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

    from color_db.utilities.table import Table
        
def main():
    
    # TEST
    t = Table()
    t.create(
        "blah",
        {
            "name": "text", 
            "description": "text"
        }
    )
    print("successfully created test table")

if __name__ == "__main__":
    main()
