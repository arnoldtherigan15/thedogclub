// Single source for the "What we still need" page (client/open-feedback/).
// Taken from the shared spreadsheet (Design feedback + Open questions). When something arrives, set its
// status to 'done' (it moves to the "Received" list), update `updated`, then commit and push.
//
// group:  'files' (photos and video to upload) | 'info' (text and links to send) | 'decide' (choices to make)
// status: 'open' | 'done'
// optional: true for nice-to-have items that do not hold up the launch
window.OPEN_ITEMS = {
  updated: '2026-11-12',
  answerBy: '2026-11-13',
  seoStart: '2026-11-16',
  feedbackDone: 21,
  feedbackTotal: 28,
  links: {
    sheet: 'https://docs.google.com/spreadsheets/d/1vneEA3jCe-mwgoh2xG2bGOXtSEw0FLwKkLqOQDk_S4c/edit?gid=1377128290#gid=1377128290',
    feedbackTab: 'https://docs.google.com/spreadsheets/d/1vneEA3jCe-mwgoh2xG2bGOXtSEw0FLwKkLqOQDk_S4c/edit?gid=1532930764#gid=1532930764',
    drive: 'https://drive.google.com/drive/folders/1G4COd-3CbxeS89gRgbDcsVot63bnGb4a',
    preview: 'https://develop--thedogclub-staging.netlify.app',
  },

  items: [
    // Photos and video
    { group: 'files', status: 'open', ref: 'Feedback #26 · Q-27', where: 'Photo → 8. About Us',
      title: 'Team photo beside "Our Vision"',
      text: 'The photo on the right of Our Vision in your updated Canva (page 13). A stand-in team photo is shown until it arrives.',
      img: 'img/vision-photo.jpg', imgAlt: 'The team photo on the right of Our Vision in the Canva design' },
    { group: 'files', status: 'open', ref: 'Feedback #26 · Q-27', where: 'Photo → 8. About Us',
      title: 'Photo for "Our Values"',
      text: 'Team members with dogs at the Halloween event (Canva page 14). A stand-in photo is shown until it arrives.',
      img: 'img/values-photo.jpg', imgAlt: 'The Our Values photo in the Canva design' },
    { group: 'files', status: 'open', ref: 'Feedback #24 · Q-29', where: 'Photo → 3. Facility',
      title: 'Video for the "Our Facility" background',
      text: 'The current photo stays until the video arrives; then it switches over.' },
    { group: 'files', status: 'open', ref: 'Q-09', where: 'Photo → 4. House Rules',
      title: 'Photo behind the House Rules card',
      text: 'Dogs in front of the HOTEL sign, as in your design. A park photo is used until then, also behind the FAQ.',
      img: 'img/house-rules-page.jpg', imgAlt: 'The House Rules page in the Canva design, with dogs in front of the HOTEL sign' },
    { group: 'files', status: 'open', ref: 'Feedback #5 · Q-05', where: 'Photo → 1. Service',
      title: 'Retail, Training and Homecare cards',
      text: 'One photo and one sentence for each, so the service cards match the list of services.' },
    { group: 'files', status: 'open', optional: true, ref: 'Feedback #6', where: 'Photo → 3. Facility → Mansion',
      title: 'Sharper Mansion photos',
      text: 'The two we have are small (1086 px wide) and look soft on large screens.' },
    { group: 'files', status: 'open', optional: true, ref: 'Feedback #15', where: 'Photo → 2. Loc',
      title: 'Branch photos in similar light',
      text: 'One photo per branch, taken from a similar angle and time of day, so the four cards look even.' },

    // Text and links
    { group: 'info', status: 'open', ref: 'Feedback #9',
      title: 'A few facts for About Us',
      text: 'For example the year The Dog Club started, the number of branches, or how many dogs you have cared for.' },
    { group: 'info', status: 'open', ref: 'Feedback #13',
      title: 'Form link for investor and franchise enquiries',
      text: 'Once confirmed with Welliam. It becomes a second button next to "Partner with us".' },
    { group: 'info', status: 'open', ref: 'Q-01',
      title: 'Friends of The Dog Club reward amounts',
      text: 'The flyer says IDR 100K; the Loyalty sheet says IDR 50K for the new customer and IDR 200K for the referrer. Which is right? The card shows no amounts until then.' },
    { group: 'info', status: 'open', optional: true, ref: 'Feedback #12',
      title: 'Dog Club Goods: product list',
      text: 'Name, price and photo for each product, if you would like this section. It is not in the current design, so we confirm the details with you before building.' },
    { group: 'info', status: 'open', optional: true, ref: 'Q-11',
      title: 'TDC Story video on YouTube',
      text: 'When it is uploaded, send the link and the video plays from YouTube, which is lighter on phones.' },

    // Choices
    { group: 'decide', status: 'open', ref: 'Feedback #5',
      title: 'What should each service card link to?',
      text: 'A) a Book button that opens the branch WhatsApp or Pawsi registration, or B) a page with more detail for each service.' },
    { group: 'decide', status: 'open', ref: 'Q-28',
      title: 'Is the place for Vision, Mission & Values OK?',
      text: 'They sit right after the About Us text, without their own link in the menu, because the header has no room for a ninth link.' },
    { group: 'decide', status: 'open', ref: 'Q-13',
      title: 'Remove the 4 old blog articles?',
      text: '"Tips for New Dog Owners", "Bali’s Top 10 Natural Treat and Supplement", "How to Help Your Dog Overcome Separation Anxiety" and "Bali’s Best Dog-Friendly Spots" are not in the new design. If removed, their old links go to the homepage, so nobody lands on an error page.' },
  ],
};
