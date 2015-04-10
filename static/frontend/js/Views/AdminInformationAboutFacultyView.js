var AdminInformationAboutFacultyView = BaseView.extend({

    template: _.template($("#adminAllFacultyInfoTemplate").html()),

    initialize: function(options) {
        this.model = options.faculty;
    },

    _attachEvents: function() {
        this.$('#saveFacultyInformation').on('click', $.proxy(this._addInformation, this))
    },

    _addInformation: function() {

    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }

});