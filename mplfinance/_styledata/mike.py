style = dict(style_name    = 'mike',
             base_mpl_style= 'dark_background', 
             marketcolors  = {'candle'  : {'up':'#000000', 'down':'#0080ff'},
                              'edge'    : {'up':'#ffffff', 'down':'#0080ff'},
                              'wick'    : {'up':'#ffffff', 'down':'#ffffff'},
                              'ohlc'    : {'up':'#ffffff', 'down':'#ffffff'},
                              'volume'  : {'up':'#7189aa', 'down':'#7189aa'},
                              'vcdopcod': False, # Volume Color Depends On Price Change On Day
                              'alpha'   : 1.0,
                             },
             mavcolors     = ['#ec009c','#78ff8f','#fcf120'],
             y_on_right    = True,
             gridcolor     = None,
             gridstyle     = None,
             facecolor     = None,
             rc            = [ ('axes.edgecolor'  , 'white'   ),
                               ('axes.linewidth'  ,  1.5      ),
                               ('axes.labelsize'  , 'large'   ),
                               ('axes.labelweight', 'semibold'),
                               ('axes.grid'       , True      ),
                               ('axes.grid.axis'  , 'both'    ),
                               ('axes.grid.which' , 'major'   ),
                               ('grid.alpha'      ,  0.9      ),
                               ('grid.color'      , '#b0b0b0' ),
                               ('grid.linestyle'  , '--'      ),
                               ('grid.linewidth'  ,  0.8      ),
                               ('figure.facecolor', '#0a0a0a' ),
                               ('patch.linewidth' ,  1.0      ),
                               ('lines.linewidth' ,  1.0      ),
                               ('font.weight'     , 'medium'  ),
                               ('font.size'       ,  10.0     ),
                               ('figure.titlesize', 'x-large' ),
                               ('figure.titleweight','semibold'),
                             ],
             base_mpf_style= 'mike'
            )