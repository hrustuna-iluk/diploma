var AttendanceCollection = Backbone.Collection.extend({

    url: "/api/attendances",

    model: AttendanceModel

});