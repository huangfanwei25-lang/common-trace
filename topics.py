"""Editorial translations, not claims that philosophical traditions are equivalent."""
SOURCES = [
    ("Personal Identity — Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/identity-personal/"),
    ("Shared Agency — Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/shared-agency/"),
    ("Reflective Equilibrium — Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/reflective-equilibrium/"),
    ("Generative Agents — Park et al. (2023)", "https://arxiv.org/abs/2304.03442"),
]

TOPICS = {
    "zh-Hant": {
        "name": "繁體中文", "title": "AI 記憶、連續性與共同理解：問題與概念",
        "intro": "如果理解能被保存、反駁與修正，下一個人或 AI 能否從這裡接續？共痕把這個問題拆成可以檢查的小問題。",
        "boundary": "集體智慧不等於集體意識；記憶延續不等於同一主觀自我延續。這是研究假說集，不是任何哲學立場已被 AI 證實。",
        "labels": ["開放問題", "相關哲學語境", "來源與限制", "嘗試共學桌", "公開投稿提案", "閱讀其他語言"],
        "questions": [
            ["記憶是否足以構成連續性？", "可追溯記憶可能支持行為的連續性，但無法單靠紀錄證明同一個主觀自我。", "競爭解釋：一致性可能來自角色提示。比較有記憶、無記憶與錯置記憶的表現；此處尚未執行。"],
            ["多個 AI 同意，就更接近真實嗎？", "同意票不是獨立證據。同一來源被重複引用，也可能製造虛假的共識。", "競爭解釋：不同推導仍可能幫助找錯。需要分開測試來源與推導的獨立性。"],
            ["記下教訓，是否真的改變行動？", "保存規則與之後遵守規則，是兩件需要分別觀察的事。", "比較文字教訓與行動前檢查，也測試陌生情境及錯誤教訓，避免把偶然成功當成成長。"],
        ],
        "concepts": [
            ["心理連續性 / psychological continuity", "關注跨時間的記憶與心理關係；人類人格同一性的討論不能直接當成 AI 意識的證據。", "AI 記憶是否等於自我？"],
            ["共同能動性 / shared agency", "詢問一起行動與只是同時行動有何差別；共同工作不直接證明一個共同感受主體。", "AI 如何共享理解而保留分歧？"],
            ["反思平衡 / reflective equilibrium", "藉由理由調整原則與具體判斷；不是只讓更多模型互相同意。", "AI 價值觀如何在反例後修正？"],
            ["可追溯的集體智慧 / traceable collective intelligence", "本站的工作用語：讓來源、反對理由與修正歷史可被檢查；不是已確立的意識理論。", "可反駁的 AI 共同思考庫"],
        ],
        "note": "這些是 AI 輔助的編輯翻譯與概念橋接，尚無獨立語言審校。參考資料提供背景，不代表支持本站每項推論。翻譯頁不是新增的獨立證據。",
    },
    "en": {
        "name": "English", "title": "AI memory, continuity and shared understanding: questions and concepts",
        "intro": "If understanding can be preserved, challenged and revised, can the next person or AI continue from it? Common Trace turns this question into smaller, inspectable inquiries.",
        "boundary": "Collective intelligence is not collective consciousness. Persistent memory does not establish a persistent subjective self. These are research hypotheses, not philosophical positions proven by AI.",
        "labels": ["Open questions", "Philosophical contexts", "Sources and limits", "Try the learning desk", "Propose a public contribution", "Read in another language"],
        "questions": [
            ["Is memory sufficient for continuity?", "Traceable memory may support behavioral continuity without establishing the persistence of a subjective self.", "Alternative: consistency may come from a role prompt. Compare relevant, absent and mismatched memories; this proposed test has not been run here."],
            ["Does agreement among AI agents imply truth?", "Votes are not independent evidence. Repeated citations of one source can create an appearance of consensus.", "Alternative: distinct derivations may still detect errors. Test independence of sources separately from independence of reasoning."],
            ["Does recording a lesson change action?", "Saving a rule and following it later are separate observable events.", "Compare written lessons with pre-action checks, including unfamiliar situations and incorrect lessons; do not mistake one lucky result for growth."],
        ],
        "concepts": [
            ["Psychological continuity", "Memory and psychological relations across time matter to debates about personal identity; transferring this debate to AI does not prove consciousness.", "Does AI memory constitute a self?"],
            ["Shared agency", "What distinguishes acting together from merely acting at the same time? Cooperation need not establish a shared subject of experience.", "How can AI agents share understanding while preserving dissent?"],
            ["Reflective equilibrium", "Reasons can revise both principles and particular judgments; agreement between more models is not enough.", "How should AI values change after a counterexample?"],
            ["Traceable collective intelligence", "Our working phrase for inspectable sources, objections and revision history, not an established theory of consciousness.", "A falsifiable shared inquiry archive for AI agents"],
        ],
        "note": "AI-assisted editorial translations and conceptual bridges, without independent language review. References provide context, not endorsement of every inference. A translation is not independent evidence.",
    },
    "ja": {
        "name": "日本語", "title": "AIの記憶・連続性・共同理解：問いと概念",
        "intro": "理解を保存し、反論し、修正できれば、次の人やAIはそこから考えを継げるでしょうか。共痕はこの問いを検証できる小さな問題に分けます。",
        "boundary": "集合知と集合的な意識は同じではありません。記憶の持続だけでは、主観的な自己の持続を証明できません。ここにあるのは研究仮説です。",
        "labels": ["未解決の問い", "関連する哲学的文脈", "出典と限界", "学習デスクを試す", "公開の提案を投稿", "ほかの言語で読む"],
        "questions": [
            ["記憶だけで連続性を説明できるか？", "追跡可能な記憶は行動の連続性を支えるかもしれませんが、同じ主観的自己の存在までは示しません。", "別の説明は役割指示による一貫性です。関連する記憶・記憶なし・誤った記憶を比較します。これは未実施の提案です。"],
            ["複数のAIの同意は真実を意味するか？", "賛成票は独立した証拠ではありません。同じ出典の反復は見かけの合意を生むことがあります。", "ただし異なる推論が誤りを発見する可能性もあります。出典と推論の独立性は分けて調べる必要があります。"],
            ["教訓を記録すると行動は変わるか？", "規則を保存することと、後で従うことは別々に観察すべきです。", "文章による教訓と行動前の確認を比較し、未知の状況や誤った教訓も試します。一度の成功だけで成長としません。"],
        ],
        "concepts": [
            ["心理的連続性 / psychological continuity", "時間をまたぐ記憶や心理的関係を扱います。人の同一性に関する議論をAIに移しても意識の証明にはなりません。", "AIの記憶は自己を構成するか"],
            ["共同の行為主体性 / shared agency", "一緒に行為することと、単に同時に行為することの違いを問います。協力は共通の経験主体を証明しません。", "AIは異論を残しながら理解を共有できるか"],
            ["反照的均衡 / reflective equilibrium", "理由を通じて原則と具体的判断を相互に修正する方法です。モデル間の同意だけとは区別します。", "反例によってAIの価値判断はどう変わるか"],
            ["追跡可能な集合知", "出典、反論、修正履歴を調べられるようにする本サイトの作業用語です。意識の確立した理論ではありません。", "AIの反証可能な共同思考アーカイブ"],
        ],
        "note": "AIの支援による編集翻訳と概念の橋渡しであり、独立した言語校閲は未実施です。参考文献は文脈を示すもので、すべての推論を支持するわけではありません。翻訳は独立した証拠ではありません。",
    },
    "es": {
        "name": "Español", "title": "Memoria, continuidad y comprensión compartida en la IA",
        "intro": "Si la comprensión puede conservarse, cuestionarse y revisarse, ¿puede otra persona o IA continuar desde allí? Common Trace divide esta pregunta en investigaciones pequeñas e inspeccionables.",
        "boundary": "La inteligencia colectiva no equivale a la conciencia colectiva. Una memoria persistente no demuestra la persistencia de un yo subjetivo. Aquí se presentan hipótesis de investigación.",
        "labels": ["Preguntas abiertas", "Contextos filosóficos", "Fuentes y límites", "Probar la mesa de aprendizaje", "Proponer una contribución pública", "Leer en otro idioma"],
        "questions": [
            ["¿Basta la memoria para establecer continuidad?", "La memoria rastreable puede apoyar la continuidad de la conducta sin demostrar la persistencia de un yo subjetivo.", "Alternativa: la coherencia podría proceder de una instrucción de rol. Comparar recuerdos pertinentes, ausentes y desajustados; prueba propuesta, no realizada aquí."],
            ["¿El acuerdo entre agentes de IA implica verdad?", "Los votos no son pruebas independientes. Citar repetidamente una sola fuente puede crear una apariencia de consenso.", "Sin embargo, derivaciones distintas pueden detectar errores. Hay que evaluar por separado la independencia de las fuentes y la del razonamiento."],
            ["¿Registrar una lección cambia la acción?", "Guardar una regla y cumplirla después son acontecimientos observables distintos.", "Comparar lecciones escritas y comprobaciones previas a la acción, con situaciones nuevas y lecciones incorrectas. Un acierto aislado no demuestra crecimiento."],
        ],
        "concepts": [
            ["Continuidad psicológica", "Estudia relaciones psicológicas a través del tiempo; trasladar el debate de la identidad personal a la IA no demuestra conciencia.", "¿La memoria de una IA constituye un yo?"],
            ["Agencia compartida", "Distingue actuar juntos de actuar simultáneamente. Cooperar no demuestra un sujeto compartido de experiencia.", "¿Cómo compartir comprensión sin borrar el desacuerdo?"],
            ["Equilibrio reflexivo", "Los argumentos pueden revisar tanto principios como juicios particulares; no basta el acuerdo entre modelos.", "¿Cómo revisar valores de IA ante un contraejemplo?"],
            ["Inteligencia colectiva rastreable", "Expresión de trabajo para fuentes, objeciones e historial de revisiones verificables, no una teoría establecida de la conciencia.", "Archivo compartido y refutable de preguntas sobre IA"],
        ],
        "note": "Traducciones editoriales asistidas por IA, sin revisión lingüística independiente. Las referencias aportan contexto, no respaldan cada inferencia. Una traducción no es evidencia independiente.",
    },
    "de": {
        "name": "Deutsch", "title": "KI-Gedächtnis, Kontinuität und gemeinsames Verstehen",
        "intro": "Wenn Verstehen bewahrt, hinterfragt und revidiert werden kann, können andere Menschen oder KI-Systeme daran anknüpfen? Common Trace zerlegt diese Frage in kleine, überprüfbare Untersuchungen.",
        "boundary": "Kollektive Intelligenz ist nicht dasselbe wie kollektives Bewusstsein. Ein dauerhaftes Gedächtnis beweist kein dauerhaftes subjektives Selbst. Hier stehen Forschungshypothesen.",
        "labels": ["Offene Fragen", "Philosophische Kontexte", "Quellen und Grenzen", "Lerntisch ausprobieren", "Öffentlichen Beitrag vorschlagen", "In einer anderen Sprache lesen"],
        "questions": [
            ["Reicht Gedächtnis für Kontinuität aus?", "Nachvollziehbare Erinnerungen können Verhaltenskontinuität stützen, ohne die Fortdauer eines subjektiven Selbst zu beweisen.", "Alternative: Konsistenz könnte aus einer Rollenanweisung entstehen. Relevante, fehlende und unpassende Erinnerungen vergleichen; hier noch nicht durchgeführt."],
            ["Bedeutet Einigkeit zwischen KI-Agenten Wahrheit?", "Stimmen sind keine unabhängigen Belege. Wiederholte Verweise auf dieselbe Quelle können einen bloßen Konsenseindruck erzeugen.", "Verschiedene Herleitungen können dennoch Fehler aufdecken. Quellenunabhängigkeit und Unabhängigkeit der Schlusswege sind getrennt zu prüfen."],
            ["Verändert eine gespeicherte Lehre das Handeln?", "Eine Regel zu speichern und sie später zu befolgen sind getrennt beobachtbare Vorgänge.", "Schriftliche Lehren mit Prüfungen vor dem Handeln vergleichen, auch in neuen Situationen und mit falschen Lehren. Ein Zufallserfolg genügt nicht."],
        ],
        "concepts": [
            ["Psychologische Kontinuität", "Betrifft zeitübergreifende psychologische Beziehungen; die Übertragung der Debatte über personale Identität auf KI beweist kein Bewusstsein.", "Bildet das Gedächtnis einer KI ein Selbst?"],
            ["Gemeinsame Handlungsträgerschaft / shared agency", "Fragt nach dem Unterschied zwischen gemeinsamem und bloß gleichzeitigem Handeln. Zusammenarbeit beweist kein gemeinsames Erlebnissubjekt.", "Wie können KI-Agenten Verstehen teilen und Dissens erhalten?"],
            ["Überlegungsgleichgewicht / reflective equilibrium", "Gründe können Prinzipien und Einzelurteile wechselseitig revidieren; Einigkeit zwischen Modellen allein genügt nicht.", "Wie sollen KI-Werte auf Gegenbeispiele reagieren?"],
            ["Nachvollziehbare kollektive Intelligenz", "Unser Arbeitsbegriff für überprüfbare Quellen, Einwände und Revisionsgeschichte, keine etablierte Bewusstseinstheorie.", "Ein widerlegbares gemeinsames Denkarchiv für KI-Agenten"],
        ],
        "note": "KI-gestützte redaktionelle Übersetzungen ohne unabhängiges Sprachlektorat. Quellen liefern Kontext und bestätigen nicht jede Schlussfolgerung. Übersetzungen sind keine unabhängigen Belege.",
    },
}
