// References Provider
'use strict';

import { TextDocument, Position, ReferenceContext, Location, workspace } from "vscode";
import { getKeywordPrefix } from "./extension";
import { NavigationData } from "./navigationdata";

/**
 * Returns an array of Locations that describe all matches for the keyword at the current position
 * @param document - The current text document
 * @param position - The current position
 * @param context - The current context
 * @returns An array of Locations that match the word at the current position in the current document
 */
export async function findAllReferences(document: TextDocument, position: Position, context: ReferenceContext): Promise<Location[] | null | undefined> {
    const range = document.getWordRangeAtPosition(position);
    let keyword = document.getText(range);
    if (!keyword) {
        return;
    }

    if (range) {
        const prefix = getKeywordPrefix(document, position, range);
        if (prefix && prefix !== 'store') {
            keyword = `${prefix}.${keyword}`;
        }
    }

    let references: Location[] = [];
    const files = await workspace.findFiles('**/*.rpy');
    if (files && files.length > 0) {
        for (let file of files) {
            document = await workspace.openTextDocument(file);
            const locations = findReferenceMatches(keyword, document);
            if (locations) {
                for (let l of locations) {
                    references.push(l);
                }
            }
        }
    }

    return references;
}

/**
 * Returns a list of locations for the given document where they keyword is found
 * @param keyword - The keyword to search for
 * @param document - The TextDocument to search
 * @returns An array of Locations that match the keyword in the given document
 */
export function findReferenceMatches(keyword: string, document: TextDocument): Location[] {
	let locations: Location[] = [];
	const rx = RegExp(`[^a-zA-Z_](${keyword.replace('.','/.')})[^a-zA-Z_]`, 'g');

	let index = 0;
	while (index < document.lineCount) {
		let line = NavigationData.filterStringLiterals(document.lineAt(index).text);
		let matches = rx.exec(line);
		if (matches) {
			let position = new Position(index, matches.index);
			const loc = new Location(document.uri, position);
			locations.push(loc);
		}
		index++;
	}

	return locations;
}
