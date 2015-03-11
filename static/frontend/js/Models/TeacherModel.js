var TeacherModel = Backbone.Model.extend ({

    urlRoot: '/api/teacher',

    defaults: function() {
        return {
            name: "",
            surname: "",
            middleName: "",
            position: PositionModel,
            department: DepartmentModel
        }
    },

    setSurname: function(value) {
        this.set("surname", value);
    },

    getSurname: function() {
        return this.get("surname");
    },

    setName: function(value) {
        this.set("name", value);
    },

    getName: function() {
        return this.get("name");
    },

    setMiddleName: function(value) {
        this.set("middleName", value);
    },

    getMiddleName: function() {
        return this.get("middleName");
    }

});