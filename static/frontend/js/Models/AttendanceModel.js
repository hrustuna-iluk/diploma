var AttendanceModel = Backbone.Model.extend({

    urlRoot: '/api/attendance/',

    defaults: function() {
        return {
            startDate: '',
            endDate: '',
            group: GroupModel,
            amountOfWeeks: 0
        }
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }
});