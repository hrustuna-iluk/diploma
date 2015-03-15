var WorkWithStudentModel = Backbone.Model.extend ({

    urlRoot: '/api/workwithstudent/',

    defaults: function() {
        return {
            text: "",
            year: "",
            group: GroupModel
        }
    }

});