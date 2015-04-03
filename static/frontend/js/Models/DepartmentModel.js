var DepartmentModel = Backbone.Model.extend ({

    urlRoot: '/api/department/',

    defaults: function() {
        return {
            title: "",
            specialization: "",
            headOfDepartment: null

        }
    },


    setTitle: function(value) {
        this.set('title', value);
    },

    getTitle: function() {
        return this.get('title');
    },

     setSpecialization: function(value) {
        this.set('specialization', value);
    },

    getSpecialization: function() {
        return this.get('specialization');
    },

    setHeadOfDepartment: function(value) {
        this.set('headOfDepartment', value);
    },

    getHeadOfDepartment: function() {
        return this.get('headOfDepartment');
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }
});