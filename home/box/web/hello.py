from cgi import parse_qsl

def HelloWorld(env,start_response):
	d = parse_qsl(env['QUERY_STRING'])
	output = ''
	if env['REQUEST_METHOD'] == 'GET':
		if env['QUERY_STRING'] != '':
			for ch in d:
				output.append(ch)
				output.append('\n')
	start_response('200 OK',[('Content-Type','text/plain')])
	return output