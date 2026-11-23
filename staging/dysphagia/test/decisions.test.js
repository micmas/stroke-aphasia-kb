import test from 'node:test';
import assert from 'node:assert/strict';
import {validate,onRequest,BRANCH} from '../functions/api/decisions.js';
const d={id:'DYS-0123456789abcdef',decision:'include',reason:'',notes:''};
test('rejects Aphasia IDs and requires exclusion reasons',()=>{
 assert.equal(validate({decisions:[d]}),null);
 assert.ok(validate({decisions:[{...d,id:'C123'}]}));
 assert.ok(validate({decisions:[{...d,decision:'exclude'}]}));
});
test('refuses production branch before any network request',async()=>{
 const response=await onRequest({env:{GITHUB_BRANCH:'main'}});
 assert.equal(response.status,503);
});
