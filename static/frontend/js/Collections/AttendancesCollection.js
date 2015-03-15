var AttendancesCollection = Backbone.Collection.extend({

    url: '/api/attendances',

    model: AttendanceModel

});