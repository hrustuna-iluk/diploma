var WorkWithStudentCollection = Backbone.Collection.extend({

    url: '/api/studentworks',

    model: WorkWithStudentModel

});