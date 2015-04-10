var FacultyModel = Backbone.Model.extend ({

    urlRoot: '/api/faculty/',

    defaults: function() {
        return {
            title: "",
            amountOfWeekInSecondSemester: 0,
            amountOfWeekInFirstSemester: 0,
            endSecondSemester: null,
            endFirstSemester: null,
            startSecondSemester: null,
            startFirstSemester: null,
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