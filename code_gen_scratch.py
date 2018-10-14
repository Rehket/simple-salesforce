from code_gen import BatchClassTemplate

if __name__ == '__main__':
    print('Code Gen Scratch')
    batch_class_definition = {'class_name': 'BatchClassGenTest',
                              'author': 'Adam',
                              'batch_object': 'Account',
                              'description': 'This is a test...',
                              'fields': 'Id, name',
                              'operation': 'Update'
                              }

    batch_class, test_class = BatchClassTemplate.render_batch_class(batch_class_definition)

    with open(batch_class_definition['class_name'] + '.cls', mode='w') as output:
        output.write(batch_class)
        if test_class:
            with open(batch_class_definition['class_name'] + '_Test.cls', mode='w') as test_output:
                test_output.write(test_class)
