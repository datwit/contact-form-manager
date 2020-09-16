const path = require( 'path' );

module.exports = {
    context: __dirname,
    entry: {
      app: './src/index.js',
    },
    output: {
        path: path.resolve( __dirname, '../application/static/js' ),
        filename: '[name].js',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: 'babel-loader',
            }
        ]
    },
    externals: {
    }
};
