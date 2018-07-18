import json

def retrieve_request_arguments(request, session_argument_names=None, compulsory_body_argument_names=None,
                               optional_body_argument_names=None, compulsory_query_parameters=None,
                               optional_query_parameters=None, version=False):
    session_argument_names = [] if session_argument_names is None else session_argument_names
    compulsory_body_argument_names = [] if compulsory_body_argument_names is None else compulsory_body_argument_names
    optional_body_argument_names = [] if optional_body_argument_names is None else optional_body_argument_names
    compulsory_query_parameters = [] if compulsory_query_parameters is None else compulsory_query_parameters
    optional_query_parameters = [] if optional_query_parameters is None else optional_query_parameters
    # TODO: There must be an dryer way of doing above.
    # TODO: Make all views retrieve query parameters this way
    arguments_to_return = []

    for session_argument_name in session_argument_names:
        try:
            arguments_to_return.append(request.session[session_argument_name])
        except KeyError:
            raise ValueError("The session didn't contain the argument {}".format(session_argument_name))

    if len(compulsory_body_argument_names) > 0 or len(optional_body_argument_names) > 0:
        try:
            data = json.loads(request.body)
        except ValueError:
            raise ValueError("The request body wasn't formatted properly as a json: {}".format(request.body))

        for compulsory_body_argument_name in compulsory_body_argument_names:
            try:
                arguments_to_return.append(data[compulsory_body_argument_name])
            except KeyError:
                raise ValueError("The request body didn't contain the argument '{}'".format(compulsory_body_argument_name))
        for optional_body_argument_name in optional_body_argument_names:
            arguments_to_return.append(data.get(optional_body_argument_name, None))

    if request.method in ['GET', 'POST', 'PUT', 'DELETE']:
        query_parameters = str(request.method)
    else:
        query_parameters = {}
        # Really, this shouldn't be possible. # TODO Make certain this case can't happen

    # for compulsory_query_parameter in compulsory_query_parameters:
    #     try:
    #         arguments_to_return.append(query_parameters[compulsory_query_parameter])
    #     except KeyError:
    #         raise ValueError("The query parameters didn't contain the compulsory argument {}".format(compulsory_query_parameter))

    for optional_query_parameter in optional_query_parameters:
        if request.method == 'GET':
            mstring = []
            for key in request.GET.iterkeys():
                arguments_to_return.append( str(request.GET.get(key)) )

    if len(arguments_to_return) == 1:
        return arguments_to_return[0]
    return tuple(arguments_to_return)