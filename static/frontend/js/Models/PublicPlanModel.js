var PublicPlanModel = Backbone.Model.extend ({

    urlRoot: '/api/publicplan/',

    defaults: function() {
        return {
            event: "",
            date: "",
            responsive: "",
            description: "",
            amountHours: 0,
            amountPresent: 0,
            semester: 0,
            group: null
        }
    },

    setEvent: function(value) {
        this.set('event', value);
    },

    getEvent: function() {
        return this.get('event');
    },

    setDate: function(value) {
        this.set('date', value);
    },

    getDate: function() {
        return this.get('date');
    },

    setResponsive: function(value) {
        this.set('responsive', value);
    },

    getResponsive: function() {
        return this.get('responsive');
    },

    setDescription: function(value) {
        this.set('description', value);
    },

    getDescription: function() {
        return this.get('description');
    },

    setAmountHours: function(value) {
        this.set('amountHours', value);
    },

    getAmountHours: function() {
        return this.get('amountHours');
    },

    setAmountPresent: function(value) {
        this.set('amountPresent', value);
    },

    getAmountPresent: function() {
        return this.get('amountPresent');
    },

    setSemester: function(value) {
        this.set('semester', value);
    },

    getSemester: function() {
        return this.get('semester');
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }


});