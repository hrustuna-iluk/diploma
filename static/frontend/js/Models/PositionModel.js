var PositionModel = Backbone.Model.extend({

    urlRoot: '/api/position',

    defaults: function() {
        return {
            title: "",
            isATeacher: false
        }
    }
});