var FacultyModel = Backbone.Model.extend ({

    urlRoot: '/api/faculty/',

    defaults: function() {
        return {
            title: "",
            dean: TeacherModel
        }
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }

});