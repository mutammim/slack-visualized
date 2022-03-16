# Treemap for channels

Make a [treemap](https://en.wikipedia.org/wiki/Treemapping) of the top channels in your Slack workspace!

## Usage

1. Go to your [Slack workspace analytics](https://slack.com/stats#channels), and click **Export CSV**.

   - If you adjust the time duration and columns shown, your changes should be reflected in future CSV downloads.
   - Slack will send the file over to Slackbot DMs in that workspace.
   - Move and rename this file to `data/treemap-channels.csv`, with `data` being a folder in the cloned repo.

2. Ensure you have a recent version of Python, as well as `matplotlib` and `squarify` installed.

3. Open `channels.py`, and scroll through the constants. Does it look alright?

   - Depending on what column you want determining the size of treebox columns, you may want to adjust `COLUMN_INDEX`.
   - Look at the first row of the CSV file. Count from 0, from left to right, to find the right column index.

4. Run `channels.py` with Python.

## Troubleshooting

If `treemap` is not working, here's a few things you can try:

- Update to the latest release version of Python.
- Make sure all imported packages are installed.
- Check the constant variables. Experimenting with different values could fix your issue.
