var FacultyModel = Backbone.Model.extend ({

    urlRoot: '/api/faculty/',

    defaults: function() {
        return {
            title: "",
            dean: TeacherModel,
            department: DepartmentModel

        }
    }
});