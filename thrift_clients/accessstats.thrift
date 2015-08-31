exception ServerError {
    1: string message,
}

exception ValueError {
    1: string message,
}

struct filters {
    1: string param,
    2: string value
}

struct kwargs {
    1: string key,
    2: string value,
}

service AccessStats {
    string document(1: string code, 2: string collection) throws (1:ValueError value_err, 2:ServerError server_err),
    string search(1: string body, 2: optional list<kwargs> parameters) throws (1:ValueError value_err, 2:ServerError server_err)
}