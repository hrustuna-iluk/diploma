var ClassModel = Backbone.Model.extend ({

    urlRoot: '/api/class',

    defaults: function() {
        return {
            subject: "",
            type: "",
            teacher: TeacherModel,
            classroom: ClassroomModel,
            day: "",
            numberOfWeek: 0,
            number: 0,
            schedule: ScheduleModel
        }
    }

});