var ClassView = BaseView.extend ({

    tagName: 'td',

    template:  _.template($("#classInformation").html()),

    initialize: function(options) {
        this.group = options.group;
        this.teachersCollection = options.teachersCollection;
    },

    setModel: function (model) {
        this.model = model;
        this._changeClass();
        return this;
    },

    _attachEvents: function() {
        this.$el.on('click', $.proxy(this._showModal, this));
        this.model.on('change', $.proxy(this._changeClass, this));
    },

    _changeClass: function() {
        var self = this;
        self.$el.html(this.template(this.model.toJSON()));
    },

    _showModal: function() {
        new ClassModalView ({
            group: this.group,
            model: this.model,
            teachersCollection: this.teachersCollection
        }).render().el
    },

    render: function() {
        //this.$el.html(this.model.toJSON());
        this._attachEvents();
        return this;
    }
});