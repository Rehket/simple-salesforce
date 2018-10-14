
@isTest
private class {{name}} {
	/*
	 * @description {{description}}
	 * @author {{author}}
	 * @datecreated {{date}}
	 *
	 * @changes Log any modifications here...
	 */
    @testSetup
    static void setup() {
        List<batch_object> {{batch_object_list}} = new List<batch_object>();

        // Set up test Data Here....
        for (Integer i=0;i<10;i++) {
            //Set up 10 Objects...
        }

        insert {{batch_object_list}};

    }
    static testmethod void test() {
        Test.startTest();

		//Run Your Tests Here

        Test.stopTest();

        // Performs your assertions here

    }

}