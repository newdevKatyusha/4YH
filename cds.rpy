python early:
    def parse_vl(lexer):
        base_ln = lexer.simple_expression()
        identifier = lexer.rest().strip()
        #full_vl_path = base_ln + identifier + ".ogg"
        #print("eval: ")
        #print(eval(full_ln_path))
        #return full_ln_path
        #return (base_ln, identifier)
        return (base_ln, identifier)

    def execute_ln(parsed_object):
        base_ln, identifier = parsed_object
        #print(identifier)
        #print("identifier: ", identifier.strip())
        #print("parsed_object", parsed_object)
        #print("sustain", sustain)
        full_vl_path = eval(base_ln) + str(identifier) + ".ogg"
        #print("full_path: ",full_vl_path)
        voice(full_vl_path)


    renpy.register_statement(
        "vl",
        parse=parse_vl,
        execute=execute_ln
    )