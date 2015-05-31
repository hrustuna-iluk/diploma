var TeacherModel = Backbone.Model.extend ({

    urlRoot: '/api/teacher/',

    defaults: function() {
        return {
            firstName: "",
            lastName: "",
            middleName: "",
            position: "",
            phone: "",
            email: "",
            user: UserModel,
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
    },

    getPosition: function() {
        return this.get("position");
    },

     getPhone: function() {
        return this.get("phone");
    },

    setPhone: function(value) {
        this.set("phone", value);
    },

    getEmail: function() {
        return this.get("email");
    },

    getPosition: function () {
        return this.get("position");
    },

    setEmail: function(value) {
        this.set("email", value);
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }

});