var ClassView = BaseView.extend ({

    tagName: 'td',

    className: 'classTitle',

    initialize: function() {
        this.listenTo(this.model, 'change', this.render);
    },

    _attachEvents: function() {
        this.$el.on('dblclick ', $.proxy(this._changeClass, this));
        this.$('.edit').on('keypress', $.proxy(this._updateOnEnter, this));
    },

    _changeClass: function() {},

     _close: function() {
      var value = this.input.val();
      if (!value) {
        this.clear();
      } else {
        this.model.save({subject: value});
        this.$el.removeClass("editing");
      }
    },

    _updateOnEnter: function(e) {
      if (e.keyCode == 13) this.close();
    },

    render: function() {
        this.$el.text(this.model.get('subject'));
        this.input = this.$('.edit');
        return this;
    }
});