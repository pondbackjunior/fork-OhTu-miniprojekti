reference_fields = {
    "article":       { "required": ["author", "title", "journal", "year"], 
                       "optional": ["volume", "number", "pages", "month", "note"] },
    "book":          { "required": ["author", "editor", "title", "publisher", "year"],
                       "optional": ["volume", "number", "pages", "month", "note"] },
    "booklet":       { "required": ["author", "title", "howpublished", "address", "year"],
                       "optional": ["editor", "volume", "number", "organization", "month", "note"] },
    "conference":    { "required": ["author", "title", "booktitle", "year"],
                       "optional": ["editor", "volume", "number", "pages", "address", "month", "organization", "publisher", "note"] },
    "inbook":        { "required": ["author", "title", "booktitle", "publisher", "year"],
                       "optional": ["editor", "volume", "number", "address", "edition", "month", "pages", "note"] },
    "incollection":  { "required": ["author", "title", "booktitle", "publisher", "year"],
                       "optional": ["editor", "volume", "number", "pages", "address", "month"] },
    "inproceedings": { "required": ["author", "title", "booktitle", "year"],
                       "optional": ["editor", "volume", "number", "pages", "address", "month", "organization", "publisher"] },
    "manual":        { "required": ["title", "year"],
                       "optional": ["author", "organization", "address", "edition", "month", "note"] },
    "mastersthesis": { "required": ["author", "title", "school", "year"],
                       "optional": ["type", "address", "month", "note"] },
    "misc":          { "required": [],
                       "optional": ["author", "title", "howpublished", "month", "year", "note"] },
    "phdthesis":     { "required": ["author", "title", "school", "year"],
                       "optional": ["type", "address", "month", "note"] },
    "proceedings":   { "required": ["title", "year"],
                       "optional": ["editor", "volume", "number", "series", "address", "month", "publisher"] },
    "techreport":    { "required": ["author", "title", "institution", "year"],
                       "optional": ["type", "number", "address", "month", "note"] },
    "unpublished":   { "required": ["author", "title", "note"],
                       "optional": ["month", "year"] },
}

def get_reference_fields(reference_type):
    if reference_type not in reference_fields:
        raise ValueError(f"Invalid reference type: {reference_type}")
    return reference_fields.get(reference_type, {})

def get_reference_types():
    return list(reference_fields.keys())

if __name__ == "__main__":
    # TODO delete later
    # TODO change location of this?
    
    # How to use:
    # from [minne ikinä sit tää laitetaankin].references import get_reference_fields
    
    article = get_reference_fields("article")
    print(f"article fields: \n {article}\n")

    article_required_fields = article["required"]
    print(f"article required fields: \n {article_required_fields}\n")

    all_book_fields = get_reference_fields("book")["required"] + get_reference_fields("book")["optional"]
    print(f"book reference's required and optional fields: \n {all_book_fields}\n")

    print(f"all reference types: \n {get_reference_types()}\n")
    for ref_type in get_reference_types():
        print(f"reference type: {ref_type}")
        print(f"required fields: {get_reference_fields(ref_type)['required']}")
        print(f"optional fields: {get_reference_fields(ref_type)['optional']}\n")