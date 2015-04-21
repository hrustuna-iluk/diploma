var PassModel = Backbone.Model.extend({

    urlRoot: '/api/pass/',

    defaults: function() {
        return {
            student: StudentModel,
            class_passed: ClassModel,
            date: "",
            type: ""
        }
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }
});