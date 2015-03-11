var PassView = BaseView.extend ({

    tagName: 'td',

    initialize: function() {

    },

    _attachEvents: function() {
        this.model.on('click', this._addPass);
    },

    _addPass: function() {

    },

    render: function() {
        this._attachEvents();
        return this;
    }
});