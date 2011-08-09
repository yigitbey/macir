from google.appengine.ext.db import Property

import iterableString

class iterableStringProperty(Property):
    data_type = iterableString.iterableString
    
    def get_value_for_datastore(self, model_instance):
        return str(super(iterableStringProperty, self).get_value_for_datastore(model_instance))

    def make_value_from_datastore(self, value):
        return iterableString.iterableString(value)

