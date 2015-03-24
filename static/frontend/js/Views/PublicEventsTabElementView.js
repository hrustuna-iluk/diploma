var PublicEventsTabElementView = BaseView.extend({

    template: _.template($("#publicEventTabElementTemplate").html()),

    selectors: {
        changePublicEventButton: ".change-publicEvent",
        deletePublicEventButton: ".remove-publicEvent"
    },

    _attachEvents: function() {
        this.$(this.selectors.changePublicEventButton).on("click", $.proxy(this._changePublicEvent, this));
        this.$(this.selectors.deletePublicEventButton).on("click", $.proxy(this._deletePublicEvent, this));
    },

    _changePublicEvent: function() {
        this.publisher.trigger('change public event', this.model);
    },

    _deletePublicEvent: function() {
        this.remove();
    },


    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }

});