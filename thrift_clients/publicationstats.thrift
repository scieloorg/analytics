exception ServerError {
    1: string message,
}

exception ValueError {
    1: string message,
}

struct aggs {
    1: string key,
    2: i32 count,
}

struct nested_aggs {
    1: string key,
    2: i32 count,
    3: list<aggs> nested_aggs
}

struct filters {
    1: string param,
    2: string value
}

struct kwargs {
    1: string key,
    2: string value,
}

service PublicationStats {
    string journal(1: list<string> aggs, 2: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> journal_subject_areas(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> journal_collections(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> journal_statuses(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> journal_inclusion_years(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> document_subject_areas(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    string document(1: list<string> aggs, 2: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> document_collections(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> document_publication_years(1: optional map<string,string> filters),
    list<aggs> document_languages(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> document_affiliation_countries(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    list<aggs> document_types(1: optional map<string,string> filters) throws (1:ValueError value_err, 2:ServerError server_err),
    string search(1:string doc_type, 2: string body, 3: optional list<kwargs> parameters) throws (1:ValueError value_err, 2:ServerError server_err)
}