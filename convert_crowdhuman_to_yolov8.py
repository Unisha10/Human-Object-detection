{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"README.md","path":"README.md","contentType":"file"},{"name":"augment_images.py","path":"augment_images.py","contentType":"file"},{"name":"convert_crowdhuman_to_yolov8.py","path":"convert_crowdhuman_to_yolov8.py","contentType":"file"},{"name":"dl_project.ipynb","path":"dl_project.ipynb","contentType":"file"}],"totalCount":4}},"fileTreeProcessingTime":1.823969,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":728550881,"defaultBranch":"main","name":"human_object_detection","ownerLogin":"gouravvemula0","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-12-07T02:21:13.000-05:00","ownerAvatar":"https://avatars.githubusercontent.com/u/58952267?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1701934092.0","canEdit":true,"refType":"branch","currentOid":"aeeb4ced8779539543b2e277004d38591d676230"},"path":"convert_crowdhuman_to_yolov8.py","currentUser":{"id":129335905,"login":"Unisha10","userEmail":"aryalunisha10@gmail.com"},"blob":{"rawLines":["import json","import cv2","import os","import tqdm","","def convert_crowdhuman_to_yolov8(annotation_file, output_dir):","    with open(annotation_file, 'r') as f:","        annotations = json.load(f)","","    if not os.path.exists(output_dir):","        os.makedirs(output_dir)","","    for annotation in tqdm.tqdm(annotations):","        image_id = annotation['ID']","        image_path = os.path.join(os.path.dirname(annotation_file), 'images', image_id)","        image = cv2.imread(image_path)","        image_height, image_width = image.shape[:2]","","        output_file = os.path.join(output_dir, image_id + '.txt')","        with open(output_file, 'w') as f:","            for gtbox in annotation['gtboxes']:","                if gtbox['tag'] == 'person':","                    x1, y1, w, h = gtbox['vbox']","                    x_center = (x1 + w) / 2","                    y_center = (y1 + h) / 2","                    normalized_width = w / image_width","                    normalized_height = h / image_height","","                    # Convert to YOLOv8 format","                    yolo_line = f\"{gtbox['tag']} {x_center} {y_center} {normalized_width} {normalized_height}\"","                    f.write(yolo_line + '\\n')","","# pip install opencv-python tqdm","","#python convert_crowdhuman_to_yolov8.py annotation_train.odgt yolov8_train","#python convert_crowdhuman_to_yolov8.py annotation_val.odgt yolov8_val"],"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":11,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":9,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":11,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":32,"cssClass":"pl-en"},{"start":33,"end":48,"cssClass":"pl-s1"},{"start":50,"end":60,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":29,"cssClass":"pl-s1"},{"start":31,"end":34,"cssClass":"pl-s"},{"start":36,"end":38,"cssClass":"pl-k"},{"start":39,"end":40,"cssClass":"pl-s1"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":31,"cssClass":"pl-en"},{"start":32,"end":33,"cssClass":"pl-s1"}],[],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-c1"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":19,"end":25,"cssClass":"pl-en"},{"start":26,"end":36,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-s1"},{"start":11,"end":19,"cssClass":"pl-en"},{"start":20,"end":30,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":21,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":31,"cssClass":"pl-en"},{"start":32,"end":43,"cssClass":"pl-s1"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":29,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-s"}],[{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":23,"cssClass":"pl-s1"},{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":33,"cssClass":"pl-en"},{"start":34,"end":36,"cssClass":"pl-s1"},{"start":37,"end":41,"cssClass":"pl-s1"},{"start":42,"end":49,"cssClass":"pl-en"},{"start":50,"end":65,"cssClass":"pl-s1"},{"start":68,"end":76,"cssClass":"pl-s"},{"start":78,"end":86,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":26,"cssClass":"pl-en"},{"start":27,"end":37,"cssClass":"pl-s1"}],[{"start":8,"end":20,"cssClass":"pl-s1"},{"start":22,"end":33,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":36,"end":41,"cssClass":"pl-s1"},{"start":42,"end":47,"cssClass":"pl-s1"},{"start":49,"end":50,"cssClass":"pl-c1"}],[],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":24,"cssClass":"pl-s1"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-en"},{"start":35,"end":45,"cssClass":"pl-s1"},{"start":47,"end":55,"cssClass":"pl-s1"},{"start":56,"end":57,"cssClass":"pl-c1"},{"start":58,"end":64,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":17,"cssClass":"pl-en"},{"start":18,"end":29,"cssClass":"pl-s1"},{"start":31,"end":34,"cssClass":"pl-s"},{"start":36,"end":38,"cssClass":"pl-k"},{"start":39,"end":40,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":35,"cssClass":"pl-s1"},{"start":36,"end":45,"cssClass":"pl-s"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":24,"cssClass":"pl-s1"},{"start":25,"end":30,"cssClass":"pl-s"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":35,"end":43,"cssClass":"pl-s"}],[{"start":20,"end":22,"cssClass":"pl-s1"},{"start":24,"end":26,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":35,"end":40,"cssClass":"pl-s1"},{"start":41,"end":47,"cssClass":"pl-s"}],[{"start":20,"end":28,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":32,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":37,"end":38,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":42,"end":43,"cssClass":"pl-c1"}],[{"start":20,"end":28,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":32,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":37,"end":38,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":42,"end":43,"cssClass":"pl-c1"}],[{"start":20,"end":36,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":43,"end":54,"cssClass":"pl-s1"}],[{"start":20,"end":37,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":40,"end":41,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":44,"end":56,"cssClass":"pl-s1"}],[],[{"start":20,"end":46,"cssClass":"pl-c"}],[{"start":20,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":110,"cssClass":"pl-s"},{"start":34,"end":48,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-kos"},{"start":35,"end":40,"cssClass":"pl-s1"},{"start":41,"end":46,"cssClass":"pl-s"},{"start":47,"end":48,"cssClass":"pl-kos"},{"start":49,"end":59,"cssClass":"pl-s1"},{"start":49,"end":50,"cssClass":"pl-kos"},{"start":50,"end":58,"cssClass":"pl-s1"},{"start":58,"end":59,"cssClass":"pl-kos"},{"start":60,"end":70,"cssClass":"pl-s1"},{"start":60,"end":61,"cssClass":"pl-kos"},{"start":61,"end":69,"cssClass":"pl-s1"},{"start":69,"end":70,"cssClass":"pl-kos"},{"start":71,"end":89,"cssClass":"pl-s1"},{"start":71,"end":72,"cssClass":"pl-kos"},{"start":72,"end":88,"cssClass":"pl-s1"},{"start":88,"end":89,"cssClass":"pl-kos"},{"start":90,"end":109,"cssClass":"pl-s1"},{"start":90,"end":91,"cssClass":"pl-kos"},{"start":91,"end":108,"cssClass":"pl-s1"},{"start":108,"end":109,"cssClass":"pl-kos"}],[{"start":20,"end":21,"cssClass":"pl-s1"},{"start":22,"end":27,"cssClass":"pl-en"},{"start":28,"end":37,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":40,"end":44,"cssClass":"pl-s"},{"start":41,"end":43,"cssClass":"pl-cce"}],[],[{"start":0,"end":32,"cssClass":"pl-c"}],[],[{"start":0,"end":74,"cssClass":"pl-c"}],[{"start":0,"end":70,"cssClass":"pl-c"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/gouravvemula0/human_object_detection/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/gouravvemula0/human_object_detection/security/dependabot","repoSecurityAndAnalysisPath":"/gouravvemula0/human_object_detection/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"convert_crowdhuman_to_yolov8.py","displayUrl":"https://github.com/gouravvemula0/human_object_detection/blob/main/convert_crowdhuman_to_yolov8.py?raw=true","headerInfo":{"blobSize":"1.32 KB","deleteInfo":{"deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"af280ff","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fgouravvemula0%2Fhuman_object_detection%2Fblob%2Fmain%2Fconvert_crowdhuman_to_yolov8.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"36","truncatedSloc":"29"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/gouravvemula0/human_object_detection/discussions/new","newIssuePath":"/gouravvemula0/human_object_detection/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/gouravvemula0/human_object_detection/blob/main/convert_crowdhuman_to_yolov8.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/gouravvemula0/human_object_detection/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/gouravvemula0/human_object_detection/raw/main/convert_crowdhuman_to_yolov8.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"gouravvemula0","repoName":"human_object_detection","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"convert_crowdhuman_to_yolov8","kind":"function","identStart":50,"identEnd":78,"extentStart":46,"extentEnd":1175,"fullyQualifiedName":"convert_crowdhuman_to_yolov8","identUtf16":{"start":{"lineNumber":5,"utf16Col":4},"end":{"lineNumber":5,"utf16Col":32}},"extentUtf16":{"start":{"lineNumber":5,"utf16Col":0},"end":{"lineNumber":30,"utf16Col":45}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/gouravvemula0/human_object_detection/branches":{"post":"Zmwh-LlA25GqHymyaeA4o9WeVZo21odOgcksda01Wizl-m4bAJ1GZdZHmNs8mGZCTSb-PGOy49A2kqKzdqeDIg"},"/repos/preferences":{"post":"LCKgP8do-TqwMgxtUbmGa_c0mg2ecdkRWle759mW2VzX95fG-3swY3SSsg5ldZO-_12LnUJ8ZAJH3A8Q9pohyA"}}},"title":"human_object_detection/convert_crowdhuman_to_yolov8.py at main · gouravvemula0/human_object_detection"}