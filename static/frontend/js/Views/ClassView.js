var ClassView = BaseView.extend ({

    tagName: 'td',

    template:  _.template($("#classInformation").html()),

    initialize: function(options) {
        this.group = options.group;
        this.classesCollection = options.classesCollection;
        this.teachersCollection = options.teachersCollection;
    },

    setModel: function (model) {
        this.model = model;
        this._changeClass();
        return this;
    },

    _attachEvents: function() {
        this.$el.on('click', $.proxy(this._showModal, this));
        this.$el.on('click', '.deleteClass', $.proxy(this._deleteClass, this));
        this.model.on('change', $.proxy(this._changeClass, this));
    },

    _changeClass: function() {
        var self = this;
        self.$el.html(this.template(this.model.toJSON()));
    },

    _showModal: function() {
        this.addClassModal = new ClassModalView ({
            group: this.group,
            model: this.model,
            teachersCollection: this.teachersCollection
        }).render();
        this.addClassModal.on('saved', $.proxy(function (model) {
            this.classesCollection.add(model);
        }, this))
    },

    _deleteClass: function (evt) {
        evt.stopPropagation();
        if(!confirm("Ви дійсно хочете видалити пару?")) {
            return;
        }
        var oldValues = this.model.toJSON();
        this.model.destroy();
        this.model = new ClassModel(_.pick(oldValues, 'group', 'day', 'number', 'numberOfWeek', 'semester', 'schedule'));
        this.model.on('change', $.proxy(this._changeClass, this));
        this.$el.empty();
    },

    render: function() {
        //this.$el.html(this.model.toJSON());
        this._attachEvents();
        return this;
    }
});