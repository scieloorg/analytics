exception ServerError{
    1: string message;
}

exception ValueError{
    1: string message;
}

struct kwargs {
    1: string key,
    2: string value,
}

service Citedby{
    string citedby_pid(1:required string q, 2:bool metaonly) throws (1:ServerError error_message)
    string citedby_doi(1:required string q, 2:bool metaonly) throws (1:ServerError error_message)
    string citedby_meta(1:required string title, 2:string author_surname, 3:i32 year, 4:bool metaonly) throws (1:ServerError error_message)
    string search(1: string body, 2: optional list<kwargs> parameters) throws (1:ValueError value_err, 2:ServerError server_err)
}