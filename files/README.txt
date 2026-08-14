Put your downloadable files in this folder, with these exact names so the
links on index.html work without editing anything:

    hawaii-2027-maps-colour.pdf
    hawaii-2027-budget-worksheet.xlsx
    hawaii-2027-reservation-calendar.pdf
    hawaii-2027-packing-checklist.pdf
    hawaii-2027-itinerary-cards.pdf

The budget worksheet already exists. The rest still need building.
If you rename a file, update the matching href in index.html.

ALSO PUT HERE:
    cover.jpg    your front cover, JPG or PNG, any size (bigger is fine).
                 The pages load cover.webp, not cover.jpg, so after you
                 drop in a new cover run this from the project root:

                     python convert_images.py --max-width 450 --force

                 That rebuilds cover.webp at the size the pages actually
                 display (about 35 KB instead of 583 KB). If cover.webp is
                 missing the image just hides itself, so nothing breaks.

BUILT AND READY:
    hawaii-2027-reservation-calendar.pdf
    hawaii-2027-packing-checklist.pdf
    hawaii-2027-itinerary-cards.pdf
    hawaii-2027-budget-worksheet.xlsx
    cover.jpg + cover.webp

STILL TO DO:
    hawaii-2027-maps-colour.pdf
    Re-run the atlas with a colour palette (see COLOUR_MAPS.txt), then
    combine the PNGs into one PDF.
