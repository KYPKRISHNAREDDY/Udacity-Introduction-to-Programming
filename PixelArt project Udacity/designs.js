function makeGrid() {
    //Get table
    var table = $('#pixel_canvas');
    //Get number of rows
    var rows = $('#input_height').val();
    //Get number of columns
    var columns = $('#input_width').val();

    table.children().remove();

    //For loops to generate rows
    for (var i = 0; i < rows; i++) {
        var byHeight = $('<tr></tr>');

        for (var j = 0; j < columns; j++) {
            //Append cells to rows
            $('<td></td>').appendTo(byHeight);
        }
        table.append(byHeight);
    }

    //Pick the color and define it for the cell
    table.on('click', 'td', function () {
        var pickColor = $('#colorPicker').val();
        $(this).css('background-color', pickColor);
    });

    //Reset color from the cell on double-click (to white)
    table.on('dblclick', 'td', function () {
        $(this).css('background-color', '#ffffff')
    })
}

    //Click the Create button to create a grid
$("input[type='submit']").click(function (e) {
    e.preventDefault();
    makeGrid();
});