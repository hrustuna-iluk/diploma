var GroupModel = Backbone.Model.extend ({

    urlRoot: '/api/group/',

    defaults: function() {
        return {
            cid: this.cid,
            number: 0,
            department: DepartmentModel,
            leader: null,
            deputyHeadman: null,
            organizer: null,
            culturalWork: null,
            healthWork: null,
            editorialBoard: [],
            otherTasks: [],
            yearStudy: 0,
            tuition: "",
            curator: TeacherModel
        }
    },

    setNumber: function(value) {
        this.set("number", value);
    },

    getNumber: function() {
        return this.get("number");
    },

    setYearStudy: function(value) {
        this.set("yearStudy", value);
    },

    getYearStudy: function() {
        return this.get("yearStudy");
    },

    setTuition: function(value) {
        this.set("tuition", value);
    },

    getTuition: function() {
        return this.get("tuition");
    }

});