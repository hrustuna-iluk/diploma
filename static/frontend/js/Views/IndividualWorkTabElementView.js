var IndividualWorkTabElementView = BaseView.extend({

    tagName: "tr",

    template: _.template($("#individualWorkTabElementTemplate").html()),

    selectors: {
        changeIndividualWorkButton: ".change-individualWork",
        deleteIndividualWorkButton: ".remove-individualWork"
    },

    _attachEvents: function() {
        this.$(this.selectors.changeIndividualWorkButton).on("click", $.proxy(this._changeIndividualWork, this));
        this.$(this.selectors.deleteIndividualWorkButton).on("click", $.proxy(this._deleteIndividualWork, this));
        this.model.on('change', $.proxy(this.render, this));
    },

    _changeIndividualWork: function() {
        this.publisher.trigger('change:individualWork', this.model);
    },

    _deleteIndividualWork: function() {
        this.model.destroy();
        this.remove();
    },


    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }

});