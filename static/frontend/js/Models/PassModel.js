var PassModel = Backbone.Model.extend({

    urlRoot: '/api/pass',

    defaults: function() {
        return {
            student: StudentModel,
            class: ClassModel,
            date: "",
            type: ""
        }
    }
});