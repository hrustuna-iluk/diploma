var TeachersCollection = Backbone.Collection.extend ({

    url: '/api/teachers',

    model: TeacherModel

});