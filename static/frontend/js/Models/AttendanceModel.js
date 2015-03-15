var AttendanceModel = Backbone.Model.extend({

    urlRoot: '/api/attendance/',

    defaults: function() {
        return {
            startDate: '',
            endDate: '',
            group: GroupModel,
            path: ''
        }
    }
});