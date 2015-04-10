var StudentModel = Backbone.Model.extend ({

    urlRoot: '/api/student/',

    defaults: function() {
        return {
            firstName: "",
            lastName: "",
            middleName: "",
            group: GroupModel,
            address: "",
            currentAddress: "",
            father: FatherModel,
            mother: MotherModel,
            phone: "",
            language: LanguageModel,
            benefits: BenefitsCollection,
            isProcurement: false,
            dateBirth: 0,
            nationality: "",
            maritalStatus: "",
            sex: "",
            school: "",
            email: "",
            additional: "",
            user: UserModel
        }
    },

    setName: function(value) {
        this.set('firstName', value);
    },

    getName: function() {
        return this.get('firstName');
    },

    setSurname: function(value) {
        this.set('lastName', value);
    },

    getSurname: function() {
        return this.get('lastName');
    },

    setMiddleName: function(value) {
        this.set('middleName', value);
    },

    getMiddleName: function() {
        return this.get('middleName');
    },

    setAddress: function(value) {
        this.set('address', value);
    },

    getAddress: function() {
        return this.get('address');
    },

    setPhone: function(value) {
        this.set('phone', value);
    },

    getPhone: function() {
        return this.get('phone');
    },

    setGroup: function(value) {
        this.set('group', value);
    },

    getGroup: function() {
        return this.get('group');
    },

    setLanguage: function(value) {
        this.set('language', value);
    },

    getLanguage: function() {
        return this.get('language');
    },

    setBenefits: function(value) {
        this.set('benefits', value);
    },

    getBenefits: function() {
        return this.get('benefits');
    },

    setIsProcurement: function(value) {
        this.set('isProcurement', value);
    },

    getIsProcurement: function() {
        return this.get('isProcurement');
    },

    setDateBirth: function(value) {
        this.set('dateOfBirth', value);
    },

    getDateBirth: function() {
        return this.get('dateOfBirth');
    },

    setNationality: function(value) {
        this.set('nationality', value);
    },

    getNationality: function() {
        return this.get('nationality');
    },

    setMaritalStatus: function(value) {
        this.set('maritalStatus', value);
    },

    getMaritalStatus: function() {
        return this.get('maritalStatus');
    },

    setSex: function(value) {
        this.set('sex', value);
    },

    getSex: function() {
        return this.get('sex');
    },

    setSchool: function(value) {
        this.set('school', value);
    },

    getSchool: function() {
        return this.get('school');
    },

    setAdditional: function(value) {
        this.set('additional', value);
    },

    getAdditional: function() {
        return this.get('additional');
    },

    setPublicOrders: function(value) {
        this.set('publicOrders', value);
    },

    getPublicOrders: function() {
        return this.get('publicOrders');
    },

    getCurrentAddress: function() {
        return this.get('currentAddress');
    },

    getEmail: function() {
        return this.get('email');
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }
});