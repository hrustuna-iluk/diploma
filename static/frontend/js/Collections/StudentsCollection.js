var StudentsCollection = Backbone.Collection.extend({

    url: '/api/students/',

    model: StudentModel

});