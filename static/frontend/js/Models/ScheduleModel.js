var ScheduleModel = Backbone.Model.extend ({

    urlRoot: '/api/schedule',

    defaults: function() {
        return {
            group: GroupModel
        }
    }

});