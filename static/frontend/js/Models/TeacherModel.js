var TeacherModel = Backbone.Model.extend ({

    urlRoot: '/api/teacher/',

    defaults: function() {
        return {
            firstName: "",
            lastName: "",
            middleName: "",
            position: "",
            department: DepartmentModel
        }
    },

    setSurname: function(value) {
        this.set("lastName", value);
    },

    getSurname: function() {
        return this.get("lastName");
    },

    setName: function(value) {
        this.set("firstName", value);
    },

    getName: function() {
        return this.get("firstName");
    },

    setMiddleName: function(value) {
        this.set("middleName", value);
    },

    getMiddleName: function() {
        return this.get("middleName");
    },

    setPosition: function(value) {
        this.set("position", value);
    }

});