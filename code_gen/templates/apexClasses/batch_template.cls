global class {{class_name}} implements Database.Batchable<sObject> {
	/*
	 * @description {{description}}
	 * @author {{author}}
	 * @datecreated {{date}}
	 *
	 * @changes Log any modifications here...
	 */
    global Database.QueryLocator start(Database.BatchableContext BC) {

	/*
	 * Here we get the batches of ubject we want to chage or update.
	 * Only get what you need.
	 */
		String query = 'SELECT {{fields}} FROM {{batch_object}}';
        return Database.getQueryLocator(query);
    }

    global void execute(Database.BatchableContext BC, List<{{batch_object}}> {{batch_object_list}}) {

        for({{batch_object}} obj : {{batch_object_list}})
        {
			/*
			 * Perform operations on the object list. Do not put any DML statements here.....
			 * It is a good idea to create a helper class or function to preform operations on the object list.
			 */

		}

		//Once any object manipulation is done, we perform dml operations.
        try {

			{{operation}} {{batch_object_list}};

        } catch(DmlException e) {
            System.debug(LoggingLevel.ERROR, e.getMessage());
        }

    }

    global void finish(Database.BatchableContext BC) {
	/*
	 * Complete any action you need to take after processing like generating a report on the object processed.
	 */
	}
}